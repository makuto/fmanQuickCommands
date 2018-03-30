from fman import DirectoryPaneCommand, show_alert, show_prompt, save_json, load_json
import subprocess

quickCommandsFile = 'QuickCommands.json'

def RunCommand(command):
	processedCommand = ['cmd', '/c'] + command.split(' ')
	subprocess.call(processedCommand)

class QuickCreateCommand(DirectoryPaneCommand):
	def __call__(self):
		newCommand, ok = show_prompt('Enter new command (use %f for file)', 'subl %f')
		if newCommand and ok:
			show_alert('You entered ' + newCommand)
			quickCommands = load_json(quickCommandsFile)
			existingCommands = None
			if quickCommands:
				existingCommands = quickCommands.get('commands', '')
				existingCommands.append(newCommand)
			else:
				quickCommands = {}
				existingCommands = [newCommand]

			quickCommands['commands'] = existingCommands
			save_json(quickCommandsFile, quickCommands)

""" DirectoryPaneCommand.get_chosen_files() Returns a list of the currently selected files (=the
files marked "red"). If no files are selected, returns a one-element list consisting of the file
under the cursor. If there is no file under the cursor (eg. when the current directory is empty),
then an empty list is returned.

Because the "empty directory" case is common, your plugin should handle it. A common way of doing this is:

class MyCommand(DirectoryPaneCommand):
	def __call__(self):
		chosen_files = self.get_chosen_files()
		if not chosen_files:
			show_alert('No file is selected!')
			return
"""

class QuickExecuteCommand(DirectoryPaneCommand):
	def __call__(self):
		command, ok = show_prompt('Enter command (use %f for file)', 'subl %f')
		if command and ok:
			RunCommand(command)

def QuickSetCommandAtIndex(index):
	quickCommands = load_json(quickCommandsFile)
	if not quickCommands:
		show_alert('No quick commands created')
		return

	if len(quickCommands['commands']) <= index:
		show_alert('No quick command created for ' + str(index))
		return

	commandsListStr = ''
	for command in quickCommands['commands']:
		commandsListStr += command

	commandsListStr += 'Executing ' + str(index + 1)
	show_alert(commandsListStr)

	RunCommand(quickCommands['commands'][index])

def QuickExecuteExistingCommandAtIndex(index):
	quickCommands = load_json(quickCommandsFile)
	if not quickCommands:
		show_alert('No quick commands created')
		return

	if len(quickCommands['commands']) <= index:
		show_alert('No quick command created for ' + str(index))
		return

	commandsListStr = ''
	for command in quickCommands['commands']:
		commandsListStr += command

	commandsListStr += 'Executing ' + str(index + 1)
	show_alert(commandsListStr)

	RunCommand(quickCommands['commands'][index])

#
# Set command
#
class QuickSetCommand1(DirectoryPaneCommand):
	def __call__(self):
		QuickSetCommandAtIndex(1 - 1)

class QuickSetCommand2(DirectoryPaneCommand):
	def __call__(self):
		QuickSetCommandAtIndex(2 - 1)

class QuickSetCommand3(DirectoryPaneCommand):
	def __call__(self):
		QuickSetCommandAtIndex(3 - 1)

class QuickSetCommand4(DirectoryPaneCommand):
	def __call__(self):
		QuickSetCommandAtIndex(4 - 1)

class QuickSetCommand5(DirectoryPaneCommand):
	def __call__(self):
		QuickSetCommandAtIndex(5 - 1)

#
# Execute command
#
class QuickExecuteExistingCommand1(DirectoryPaneCommand):
	def __call__(self):
		QuickExecuteExistingCommandAtIndex(1 - 1)

class QuickExecuteExistingCommand2(DirectoryPaneCommand):
	def __call__(self):
		QuickExecuteExistingCommandAtIndex(2 - 1)

class QuickExecuteExistingCommand3(DirectoryPaneCommand):
	def __call__(self):
		QuickExecuteExistingCommandAtIndex(3 - 1)

class QuickExecuteExistingCommand4(DirectoryPaneCommand):
	def __call__(self):
		QuickExecuteExistingCommandAtIndex(4 - 1)

class QuickExecuteExistingCommand5(DirectoryPaneCommand):
	def __call__(self):
		QuickExecuteExistingCommandAtIndex(5 - 1)