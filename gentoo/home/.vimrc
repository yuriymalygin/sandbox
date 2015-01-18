" ============================================================================
"  Vim main settings
" ============================================================================

" Automatic reloading of .vimrc
autocmd! bufwritepost .vimrc source %

" Better copy & paste
set pastetoggle=<F2>
set clipboard=unnamed

" Mouse
set mouse=a

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

" ============================================================================
" Functions 
" ============================================================================

" Create function definition for autocompletion
" Source of words is all opened buffers
set complete+=.
set complete+=b

function! WordCompletion()
  let col = col('.') - 1
  if !col || getline('.')[col - 1] !~ '\k'
    return "\<tab>"
  else
    return "\<c-p>"
  endif
endfunction

" ============================================================================
" Hotkeys 
" ============================================================================

" Map new <Leader>
let mapleader = ","

" Tabs navigation
map <Leader>n <esc>:tabprev<CR>
map <Leader>m <esc>:tabnext<CR>

" Write the file and run it through python
map <F10> :w<CR>:!php %<CR>

" Call autocompletion by Tab 
imap <tab> <c-r>=WordCompletion()<cr>

" ============================================================================
" Plugins 
" ============================================================================

" Setup Pathogen to manage plugins
" PREPARE: mkdir -p ~/.vim/{autoload,bundle}
" SETUP: curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
execute pathogen#infect()

" Settings for vim-powerline
" SETUP: git clone https://github.com/Lokaltog/vim-powerline ~/.vim/bundle/vim-powerline
set laststatus=2

" Settings for nerdtree
" SETUP: git clone https://github.com/scrooloose/nerdtree ~/.vim/bundle/nerdtree
map <C-n> :NERDTreeToggle<CR> 

" Settings for ctrlp
" SETUP: git clone https://github.com/kien/ctrlp.vim ~/.vim/bundle/ctrlp.vim
let g:ctrlp_max_height = 30
set wildignore+=*.pyc
set wildignore+=*_build/*
set wildignore+=*/coverage/*
