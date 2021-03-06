# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api

from ..vkclient.little_client import LittleClient
from ..vkclient.looper import LittleLooper

import sys
import logging
import threading

_logger = logging.getLogger(__name__)

TOKEN = '000000'

class Token(models.Model):
    _name = 'vkautomator.token'

    value = fields.Char(required=True)
    start_date = fields.Datetime(default=fields.Datetime.now)
    end_date = fields.Datetime(required=False, store=True, string="End Date", compute='_get_end_date')

    @api.depends('start_date')
    def _get_end_date(self):
        _logger.info("_get_end_date called")
        for record in self:
            if not record.end_date:
                start_date = fields.Datetime.from_string(record.start_date)
                record.end_date = start_date + timedelta(seconds=86400)
        


class VkScheduler(models.Model):
    _name = 'vkautomator.vkscheduler'

    name = fields.Char(required=True)
    updates_count = fields.Integer()
    last_modified = fields.Date()

    @api.model
    def automator_start(self):
        _logger.info("automator_start called")
        self.env['mail.channel'].message_post(
                body="Notification from Automator",
                channel_ids=[(4,1)],
                subject="Automator",
                partner_ids=[(4, 3)],)

    @api.model
    def vk_client_start(self):
        _logger.info("vk_client_start called")
        client = LittleClient(TOKEN)
        looper = LittleLooper()
        looper.set_callback(_logger.info)
        threading.Thread(target=looper.loop, args=(client.get_new_message, )).start()

    

