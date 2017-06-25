# getTP - Get Source Code TODO's for a TaskPaper formatted file

This is a quick and simple Python script that uses [Ag - The Silver Searcher](https://github.com/ggreer/the_silver_searcher) to find 'TODO' items in a source tree.

The output is formatted for the [TaskPaper](https://www.taskpaper.com/) plain text format and sent to stdout. The output can be piped to a .taskpaper file.

Nothing fancy. Ag is super fast and does the heavy lifting. The Python code formats the Ag format to TaskPaper.

* The current directory name is used for the root project name.
* Each file with TODO's are sub-projects.  The sub-project names include relative directories.
* Tasks begin with the line number of the TODO.

```markdown

gettp:

        getTP.py:
                - line: 2    Combine TODO's to a TaskPaper list
                - line: 8    todo_command = 'ag TODO'
                - line: 13   Use Ag Silver Searcher to find TODO comments in source

        README.md:
                - line: 1    # getTP - Get Source Code TODO's for a TaskPaper formatted file
                - line: 3    This is a quick and simple Python script that uses [Ag - The Silver Searcher]...

        sample\test.md:
                - line: 5    * TODO: Ad nulla ad Lorem quis et quis in in laborum incididunt adipisicing occaecat id voluptate.

```

Most IDE's have some form of task tracking already. But TaskPaper organizes task lists that are usable on any platform.

## Apps that handle the TaskPaper format

* TaskPaper files are plain text, so any text editor can view and change the tasks.
* [Vim plugin](https://github.com/davidoc/taskpaper.vim)
* [VS Code plugin](https://github.com/sandy081/vscode-todotasks)
* [Sublime Text plugin](https://github.com/aziz/PlainTasks) plugin
* [Emacs](https://github.com/jedthehumanoid/taskpaper.el)
* [Editorial](http://omz-software.com/editorial/) and [Taskmator](https://www.facebook.com/Taskmator/) on iOS
* [TaskPaper](https://www.taskpaper.com/) for macOS
* [nvALT](http://brettterpstra.com/projects/nvalt/) for macOS
* [ToDoPaper](http://widefido.com/products/todopaper/) for Windows
* [TaskPaper related projects](http://www.hogbaysoftware.com/wiki/TaskPaperRelatedProjects)