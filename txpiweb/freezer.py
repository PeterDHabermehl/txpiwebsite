#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TX-Pi website.
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software.
#
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
#
"""\
Freezes the TX-Pi web application.
"""
import os
from flask_frozen import Freezer
from webapp import app, _TXPI_IMAGES

# Treat redirects as error since the Flask test client cannot handle
# external URIs anyway
app.config['FREEZER_REDIRECT_POLICY'] = 'error'

# URL to the TX-Pi setup script
_SETUP_SCRIPT_URL = 'https://raw.githubusercontent.com/ftCommunity/tx-pi/master/setup/tx-pi-setup.sh'

_REDIRECTS = {
    '/': '/en/',
    '/tx-pi-setup.sh': _SETUP_SCRIPT_URL,
}

for img_name in _TXPI_IMAGES:
    _REDIRECTS['/images/latest_{0}'.format(img_name)] = _TXPI_IMAGES[img_name]['url']

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    with open(os.path.join(freezer.root, '_redirects'), 'w') as f:
        for k, v in _REDIRECTS.items():
            f.write('{0}    {1}    302\n'.format(k, v))
