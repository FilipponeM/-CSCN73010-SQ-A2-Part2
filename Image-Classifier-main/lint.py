#lint.py 

import sys 

from pylint import lint  

#THRESHOLD = 7 

run = lint.Run(["modelcreation", "app", "result"], exit=False) 

score = run.linter.stats.global_note 

#if score < THRESHOLD: 

    # print("Linter failed: Score < threshold value") 

    # sys.exit(1) 


sys.exit(0) 