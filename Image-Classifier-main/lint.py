#lint.py 

import sys 

from pylint import lint  

THRESHOLD = 9  

run = lint.Run(["modelcreation.py", "app.py", "result.py"], exit=False) 

score = run.linter.stats.global_note 

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 
