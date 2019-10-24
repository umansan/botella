# Copyright 2017 ACSONE SA/NV
# Copyright 2018 - Brain-tec AG - Carlos Jesus Cebrian
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import json
import mimetypes
from werkzeug import url_decode

from odoo.http import route, request

from odoo.addons.web.controllers import main
from odoo.addons.web.controllers.main import (
    _serialize_exception,
    content_disposition
)
from odoo.tools import html_escape


class ReportController(main.ReportController):

    MIMETYPES = {
        'txt': 'text/plain',
        'html': 'text/html',
        'doc': 'application/vnd.ms-word',
        'odt': 'application/vnd.oasis.opendocument.text',
        'ods': 'application/vnd.oasis.opendocument.spreadsheet',
        'pdf': 'application/pdf',
        'sxw': 'application/vnd.sun.xml.writer',
        'xls': 'application/vnd.ms-excel',
    }

    @route()
    def report_routes(self, reportname, docids=None, converter=None, **data):
        if converter != 'aeroo':
            return super(ReportController, self).report_routes(
                reportname=reportname, docids=docids, converter=converter,
                **data)
        context = dict(request.env.context)

        if docids:
            docids = [int(i) for i in docids.split(',')]
        if data.get('options'):
            data.update(json.loads(data.pop('options')))
        if data.get('context'):
            # Ignore 'lang' here, because the context in data is the
            # one from the webclient *but* if the user explicitely wants to
            # change the lang, this mechanism overwrites it.
            data['context'] = json.loads(data['context'])
            if data['context'].get('lang'):
                del data['context']['lang']
            context.update(data['context'])

        # Aeroo Reports starts here
        report_obj = request.env['ir.actions.report']
        report = report_obj._get_report_from_name(reportname)
        if context.get('print_with_sudo'):
            report = report.sudo()
        context['report_name'] = reportname
        res, extension, filename = report.with_context(context).render_aeroo(
            docids, data=data)
        mimetype = self.MIMETYPES.get(res, 'application/octet-stream')
        httpheaders = [
            ('Content-Disposition', content_disposition(filename)),
            ('Content-Type', mimetype),
            ('Content-Length', len(res))
        ]
        return request.make_response(res, headers=httpheaders)

    @route()
    def report_download(self, data, token):
        """This function is used by 'qwebactionmanager.js' in order to trigger
        the download of a py3o/controller report.

        :param data: a javascript array JSON.stringified containg report
        internal url ([0]) and type [1]
        :returns: Response with a filetoken cookie and an attachment header
        """
        requestcontent = json.loads(data)
        url, type = requestcontent[0], requestcontent[1]
        if type != 'aeroo':
            return super(ReportController, self).report_download(data, token)
        try:
            reportname = url.split('/report/aeroo/')[1].split('?')[0]
            docids = None
            if '/' in reportname:
                reportname, docids = reportname.split('/')

            # on aeroo we support docids + data
            data = url_decode(url.split('?')[1]).items()
            response = self.report_routes(
                reportname, docids=docids, converter='aeroo', **dict(data))
            # if docids:
            #     # Generic report:
            #     response = self.report_routes(
            #         reportname, docids=docids, converter='aeroo')
            # else:
            #     # Particular report:
            #     # decoding the args represented in JSON
            #     data = url_decode(url.split('?')[1]).items()
            #     response = self.report_routes(
            #         reportname, converter='aeroo', **dict(data))
            response.set_cookie('fileToken', token)
            return response
        except Exception as e:
            se = _serialize_exception(e)
            error = {
                'code': 200,
                'message': "Odoo Server Error",
                'data': se
            }
            return request.make_response(html_escape(json.dumps(error)))
