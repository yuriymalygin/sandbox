# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# Put your fun stuff here.

## Bash history
HISTSIZE="10000"
HISTFILESIZE=${HISTSIZE}
HISTCONTROL="ignorespace"
HISTTIMEFORMAT="%F %T "

# Programmable Completion for bash
source /etc/profile.d/bash-completion.sh 

# Shell options (see 'man shopt')
shopt -s cdable_vars cdspell checkjobs

## Aliases
### Usability
alias p='ping -a'
alias v='feh --fullscreen'                                                                                                                                                                    
alias S='TERM=xterm-256color; ssh'
alias c='cssh'
alias cal='cal --three --monday --color'
alias ls='ls --human-readable --color=auto'
alias ax='atool --extract'
alias less='less --no-lessopen'
alias dmesg='dmesg --human'
alias ipcalc='ipcalc -b'
alias pwg='dd if=/dev/urandom bs=1 count=9 2>/dev/null | base64'
