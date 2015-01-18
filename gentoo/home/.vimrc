" =========================
"  Vim main settings
" =========================

" Automatic reloading of .vimrc
autocmd! bufwritepost .vimrc source %

" Better copy & paste
set pastetoggle=<F2>
set clipboard=unnamed

" Mouse
set mouse=a

" Map new <Leader>
let mapleader = ","

" Tabs navigation
map <Leader>n <esc>:tabprev<CR>
map <Leader>m <esc>:tabnext<CR>

" Better moving of code blocks
vnoremap < <gv
vnoremap > >gv

" Color scheme
set t_Co=256
color wombat256mod

" Syntax highlighting
filetype off
filetype plugin indent on
syntax on

" Show line numbers and length
set number
set cursorline

" Tabs and Spaces
set tabstop=2
set shiftwidth=2
set expandtab
set smartindent

" Case insensitive search
set hlsearch
set incsearch
set ignorecase
set smartcase

" Disable backup and swap files
set nobackup
set nowritebackup
set noswapfile

" =========================
" Plugins 
" =========================

" Setup Pathogen to manage plugins
" PREPARE: mkdir -p ~/.vim/{autoload,bundle}
" SETUP: curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
execute pathogen#infect()

" Settings for vim-powerline
" SETUP: cd ~/.vim/bundle && git clone git://github.com/Lokaltog/vim-powerline.git
set laststatus=2

" Settings for nerdtree
" SETUP: cd ~/.vim/bundle && git clone git://github.com/scrooloose/nerdtree.git
map <C-n> :NERDTreeToggle<CR> 

" Settings for ctrlp
" SETUP: cd ~/.vim/bundle && git clone git://github.com/kien/ctrlp.vim.git
let g:ctrlp_max_height = 30
set wildignore+=*.pyc
set wildignore+=*_build/*
set wildignore+=*/coverage/*

" Settings for jedi-vim
" PREPARE: sudo emerge -1av dev-python/jedi
" SETUP: cd ~/.vim/bundle && git clone git://github.com/davidhalter/jedi-vim.git
let g:jedi#usages_command = "<leader>z"
let g:jedi#popup_on_dot = 0
let g:jedi#popup_select_first = 0
