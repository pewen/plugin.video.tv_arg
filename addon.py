#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2012 Tristan Fischer (sphere@dersphere.de)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from xbmcswift2 import Plugin


STRINGS = {
    'page': 30001,
    'streams': 30100,
    'videos': 30101,
    'vodcasts': 30103,
    'search': 30200,
    'title': 30201
}

STATIC_STREAMS = (
    { {
        'title': 'Educational Channel HD',
        'logo': 'edu.jpg',
        'stream_url': ('http://edu.infozen.cshls.lldns.net/infozen/edu/'
                       'edu/edu_1000.m3u8'),
    }, {                                                                        
        'title': 'Radio UNRC 97.7',
        'logo': 'unrc.gif',                                                      
        'stream_url': ('http://iphone-streaming.ustream.tv/'
			'ustreamVideo/16261918/streams/live/playlist.m3u8'),
    }, {                                                                        
        'title': 'TN Tv (Bs As)',                                            
        'logo': 'tn.jpg',                                                      
        'stream_url': ('rtsp://stream.tn.com.ar/'
			'live/tnhd1'),
    }, {                                                                        
        'title': 'TN audio (Bs As)',
        'logo': 'tn.jpg',                                                      
        'stream_url': ('rtsp://stream.tn.com.ar/'                               
                        'live/tnaudio'),
    }, {
        'title': 'Canal 13 (Bs As)',
	'logo': 'canal-13-bsas.jpg',
        'stream_url': ('rtsp://stream.eltrecetv.com.ar/live13/'
			'13tv/13tv1'),
    }, {                                                                      
        'title': 'Canal 13 (Rio Cuarto)',
        'logo': 'Canal13RioCuarto.png',
        'stream_url': ('http://iphone-streaming.ustream.tv/ustreamVideo/18376856/streams/'
			'live/playlist.m3u8'),
    }, {                                                                    
        'title': 'Canal 26 (m3u8)',
        'logo': 'canal26.jpg',                                                  
        'stream_url': ('http://live-edge01.telecentro.net.ar/live/smil:c26.smil/'
			'playlist.m3u8'),
    }, {
	'title': 'FM Milenium',
	'logo': 'edu.jpg',
	'stream_url': ('rtsp://fmmilenium.activecds.telecomcdn.com.ar/'
			'fmmilenium'),
    }, {                                                                        
        'title': 'CN23',
        'logo': 'CN23.png',
        'stream_url': ('http://190.210.73.129:'
                        '1940'),
    }, {                                                                        
        'title': 'Quatro',                                                    
        'logo': 'edu.jpg',                                                      
        'stream_url': ('rtsp://cdns840stu1021.multistream.net:80/'
			'quatrotv1live/live-400'),
    }, {                                                                        
        'title': 'Canal 9',                                                      
        'logo': 'edu.jpg',                                                      
        'stream_url': ('http://72.46.226.53/live01/_definst_/'
			'canal91/playlist.m3u8'),
    }, {                                                           
        'title': 'C5N',                                       
        'logo': 'c5n.gif',                                                    
        'stream_url': ('http://c5n.stweb.tv/c5n/live/'
			'playlist.m3u8'),
    }, {
	'title': 'AM sport AR',
	'logo': 'edu.jpg',
	'stream_url': ('http://iphone-streaming.ustream.tv/'
			'uhls/11602466/streams/live/iphone/playlist.m3u8'),
    }, {
        'title': 'Canal 10 UNC',
        'logo': 'canal10-CBA.jpeg',
        'stream_url': ('http://iphone-streaming.ustream.tv/'                
                        'ustreamVideo/18308983/streams/live/playlist.m3u8'),
    }, {
        'title': 'Canal CBA 24 N3',                                    
        'logo': 'cba-24-n3.jpg',                                         
        'stream_url': ('http://iphone-streaming.ustream.tv/'      
                        'ustreamVideo/11678041/streams/live/playlist.m3u8'),  
    }, { 
        'title': 'Radio UNC',                                   
        'logo': 'edu.jpg',                                               
        'stream_url': ('http://iphone-streaming.ustream.tv/'
                        'ustreamVideo/15400867/streams/live/playlist.m3u8'),
    }, {                                                             
	'title': 'Canal 12 CBA',
	'logo': 'edu.jpg',
	'stream_url': ('http://iphone-streaming.ustream.tv/'
			'ustreamVideo/10923213/streams/live/playlist.m3u8'),
    }, {
	'title': 'UNLP TV',
	'logo': 'UNLP.jpg',
	'stream_url': ('rtmp://163.10.0.122:80/stream/'
			'tvunlp'),
   }, {
	'title': '360 TV',
	'logo': '360TV.jpg',                                                
	'stream_url': ('http://lsdmasterhls-lh.akamaihd.net/i/masterhls_10@97032/'
			'master.m3u8'),
   }, {
	'title': 'BLUE 100.7 FM Bs As',
        'logo': 'blue-1007.jpg',                                        
	'stream_url': ('http://201.212.5.144/'
			'blue'),
   }, {                                                     
        'title': 'LV16',                                     
        'logo': 'lv16.jpg',                                    
        'stream_url': ('http://hostingystreaming.com:1935/aacplus/' 
                        '4680/playlist.m3u8'),
   }, {                                                     
        'title': 'Fm Libre Rio Cuarto',                                     
        'logo': 'FM-Libre-RioCuarto.png',                                    
        'stream_url': ('http://184.107.187.146:9122/' 
                        'fmlibre'),
   }, {                                                     
        'title': 'Fm Las Higueras',                                     
        'logo': 'fmhigueras.png',                                    
        'stream_url': ('http://188.165.236.90:' 
                        '7568'),
   }, {                                                     
        'title': 'FM Gospel Rio Cuarto',                                     
        'logo': 'fmGospel.jpg',                                    
        'stream_url': ('rtsp://wowza.aacplusargentina.com:1935/aacplus/'
                        '9220'),
   }, {
       'title': 'Radio Nacional Rock',
        'logo': 'edu.jpg',                                                  
        'stream_url': ('rtmp://186.33.232.11/rn_sc_rad39/'
			'rn_sc_rad39.stream'),
   }, {
	'title': 'Nacional Folklorica',
	'logo': 'edu.jpg',
	'stream_url': ('rtmp://186.33.232.10/rn_sc_rad38/'
			'rn_sc_rad38.stream'),
   }, {
	'title': 'Nacional Cordoba',
	'logo': 'nacional-cba.jpg',
	'stream_url': ('rtmp://186.33.227.199/rn_sc_rad7/'
			'rn_sc_rad7.stream'),
   }, {
	'title': 'AM 1110 - Radio Ciudad Bs As',
	'logo': 'AM1110.png',
	'stream_url': ('http://radios.argentina.fm/tunein.php/am1110/'
			'playlist.asx'),
  }, {
	'title': 'Nuestra Radio Cba',
	'logo': 'edu.jpg',
	'stream_url': ('http://iphone-streaming.ustream.tv/ustreamVideo/15271401/streams/'
			'live/playlist.m3u8'),
  }, {
	'title': 'America2',
	'logo': 'A24.png',
	'stream_url': ('http://iphone-streaming.ustream.tv/ustreamVideo/17916700/streams/'
			'live/playlist.m3u8'),
  }, {
        'title': 'Tango City',                                           
        'logo': 'edu.jpg',                                                      
        'stream_url': ('http://stream.tangocity.com.ar/'                    
                        'tangocity'),
  }, {
	'title': 'Nacional Clasica',
	'logo': 'edu.jpg',
	'stream_url': ('rtmp://186.33.227.21/rn_sc_rad37/'
			'rn_sc_rad37.stream'),
  }, {                                                                          
        'title': 'Senado TV',
        'logo': 'edu.jpg',
        'stream_url': ('http://mun-se-2.se.hsn.activecds.telecomcdn.com.ar/'
                        'hsn'),
  }, {                                                                          
        'title': 'Folklore Cien radios',
        'logo': 'guitarreada2.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Folklore_64000.aac'),

  }, {
        'title': 'Costumbres Argentinas Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Costumbres_Argentinas_32000.aac'),

  }, {
        'title': 'Nacional Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Nacional_64000.aac'),

  }, {
        'title': '80 y 90 Nacional Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        '80_90_Nacional_32000.aac'),

  }, {
        'title': 'Egresados 1988 Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Egresados_1988_32000.aac'),

  }, {
        'title': 'All about Tango Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'All_About_Tango_32000.aac'),
                        
 }, {
        'title': 'Todo Tango Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Todo_Tango_32000.aac'),

}, {
        'title': 'Belgrano AM 650',
        'logo': 'edu.jpg',
        'stream_url': ('http://wmserver3.aginet.com.ar:13574/;stream/'
                        '1'),

 }, {
        'title': 'Grandes del Tango Cien radios',
        'logo': 'edu.jpg',
        'stream_url': ('http://buecrplb01.cienradios.com.ar/'
                        'Grandes_del_Tango_64000.aac'),
                        
  }, {
        'title': 'Media Channel HD',
        'logo': 'media.jpg',
        'stream_url': ('http://media.infozen.cshls.lldns.net/infozen/media/'
                       'media/media_1000.m3u8'),
    },
)

plugin = Plugin()


@plugin.route('/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)


def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id


def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()
