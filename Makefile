ifndef PROBLEM
$(error PROBLEM is no set)
endif

init:
		$(info Creating structure for the problem${PROBLEM})
		@mkdir problem${PROBLEM}
		@touch problem${PROBLEM}/definition.md
		@touch problem${PROBLEM}/problem.py
		@touch problem${PROBLEM}/test.py
		@touch problem${PROBLEM}/problem.js