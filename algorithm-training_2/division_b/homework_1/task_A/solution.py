code       = int(input())
interactor = int(input())
checker    = int(input())

if interactor == 0:
  verdict = 3 if code != 0 else checker
elif interactor == 1:
  verdict = checker
elif interactor == 4:
  verdict = 3 if code != 0 else 4
elif interactor == 6:
  verdict = 0
elif interactor == 7:
  verdict = 1
else:
  verdict = interactor

print(verdict)