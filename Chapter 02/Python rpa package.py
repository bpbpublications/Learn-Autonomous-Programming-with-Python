import rpa as r 

r.init(visual_automation=False, chrome_browser=True)
r.url('https://www.google.com/')
r.type('//*[@name="q"]', 'news')
r.click('//*[@name="btnK"]')
r.wait(5) # ensure results are fully loaded
r.snap('page', 'Captured_Image.png')
r.close()
