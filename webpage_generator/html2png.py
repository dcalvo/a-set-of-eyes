from selenium import webdriver
import os
import sys
import generate

# Set up browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path="C:/tools/chromedriver.exe", options=chrome_options)

# Input and output directories
html_dir = 'file:///' + os.path.join(sys.path[0], "html")
out_dir = os.path.join(sys.path[0], "png")
num_of_samples = 100 # number of gui/png pairs to generate

for i in range(num_of_samples):
    id = str(i).zfill(len(str(num_of_samples)))
    generate.generate(id, False)
    driver.get(html_dir + "/" + id + ".html")
    el = driver.find_element_by_tag_name('body')
    driver.set_window_size(1920, el.size["height"] + 1000)
    el.screenshot(out_dir + "/" + id + ".png")
    print(id)
driver.quit()