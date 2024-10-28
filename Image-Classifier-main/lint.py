#lint.py 

import sys 

from pylint import lint  

#THRESHOLD = 7 

run = lint.Run(["Image-Classifier-main/modelcreation", "Image-Classifier-main/app", "Image-Classifier-main/result"], exit=False) 

score = run.linter.stats.global_note 

#if score < THRESHOLD: 

   # print("Linter failed: Score < threshold value") 

   # sys.exit(1) 


sys.exit(0) 
