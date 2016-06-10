import re
import sys
def ChineseCharacterFind():
    f=open(r'C:\Users\Administrator\Desktop\hello.txt','r',encoding='utf-8');
    pattern=re.compile(r'[\u4e00-\u9fa5]+')
    try:
        text=f.read();
        array=pattern.findall(text)
        print(array)
    finally:
          f.close();

        
    
    
    



    
    
        
    

  
 
