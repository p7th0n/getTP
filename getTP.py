'''
Combine TODO's to a TaskPaper list
'''

import os
import subprocess

todo_command = 'ag TODO'


def find_todos():
    '''
    Use Ag Silver Searcher to find TODO comments in source
    '''
    proc = subprocess.Popen(todo_command, stdout=subprocess.PIPE)
    output = proc.stdout.read()

    project_dir = os.getcwd()
    print project_dir[project_dir.rfind(os.path.sep) + 1:] + ':'

    l = output.split('\n')
    project = ''
    for line in l:
        proj_pos = line.find(':')
        next_project = line[:proj_pos]
        is_taskpaper = next_project[next_project.rfind('.'):].lower() == '.taskpaper'
        if len(next_project.strip()) > 0 and not is_taskpaper:
            tmp_todo = line[proj_pos + 1:]
            line_num = line[proj_pos + 1:proj_pos + tmp_todo.find(':') + 1]
            todo = line[proj_pos + tmp_todo.find(':') + 2:].strip()

            if next_project == project:
                print '\t\t- line: ' + line_num.ljust(5) + todo
            else:
                project = next_project
                print '\n\t' + project + ':'
                print '\t\t- line: ' + line_num.ljust(5) + todo


if __name__ == '__main__':
    find_todos()
