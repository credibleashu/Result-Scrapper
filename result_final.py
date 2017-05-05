from selenium import webdriver
browser = webdriver.Firefox()

browser.get("http://dolphintechnologies.in/manit/results.html")

schno=browser.find_element_by_id("scholar")
type(schno)

sem=browser.find_element_by_id("semester")
submit=browser.find_element_by_id("button")

file = open("Result.txt",'w')
count=1
start_num= 141112001
end_num = 141112051
sem_num = 3
for i in range(start_num,end_num):
    try:
        t=''
        schno=browser.find_element_by_id("scholar")
        schno.click()
        schno.send_keys(i)
        sem=browser.find_element_by_id("semester")
        sem.send_keys(str(sem_num))
        submit=browser.find_element_by_id("button")
        submit.click()
        for x in browser.find_elements_by_class_name('style16'):
            t=x.text
            if(t.find("SGPA")!=-1):
                break;
        num=1
        for x in browser.find_elements_by_class_name('style3'):
            if(num==5):
                break
            num=num+1
        if(t==''):
            file.write(str(i))
            file.write(" Result Not Found\n")
        else:
            file.write(str(i))
            file.write("\t")
            file.write(x.text)
            file.write("\t")
            file.write(t)
            file.write("\n")
        browser.get("http://dolphintechnologies.in/manit/results.html")
    except Exception as ex:
        count = count + 1
        print("Error : ",ex ," at " ,i)
        browser.get("http://dolphintechnologies.in/manit/results.html")
        if(count==10): # if 10 errors have occurred
            file.close()
            break;
    #browser.back()
file.close()

