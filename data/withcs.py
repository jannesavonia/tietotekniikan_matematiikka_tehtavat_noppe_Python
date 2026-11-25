import glob
import os

def removepy(ask=True):
    python_assignments = glob.glob('???/src/my_code.py')
    print('Found following Python assignments')
    for a in python_assignments:
        print(a)

    print()

    cs_assignments = glob.glob('???/src/my_code.cs')
    print('Found following C# assignments')
    for a in cs_assignments:
        print(a)
    print()

    print('WARNING: You are about to choose C# assignments.')
    print('Selection can\'t be undo. Are you sure?')
    if ask:
        cont=input('Type YES to continue. Use capital letters!')
        if cont!='YES':
            print('Exit...')
            return

    print('Delete Python assignments...')
    for a in python_assignments:
        print('  '+a)
        os.remove(a)

if __name__=="__main__":
    removepy()
