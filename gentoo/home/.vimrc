" User Interface and Usability
set background=dark
colorscheme solarized
set cursorline
set number

" Syntax Highlighting
syntax enable
filetype on 
filetype indent plugin on

" Tabs and Spaces
set tabstop=2
set shiftwidth=2
set expandtab
set smartindent

" Mouse
set mouse=a

" CFEngine
au BufRead,BufNewFile *.cf set ft=cfengine
