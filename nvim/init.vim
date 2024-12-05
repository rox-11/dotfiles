
"   _____    __    __   ______    __     __
"  /   . \  /  \  /  \ /      \  /  \   /  \   configured by (@snom)
"  |  ___/`~|   \ |  | |  []  |  |   \ /   |
"  | |____  |  \ \|  | |  ||  |  |         |
"  |____  | |  |\    | |  ||  |  |  |\_/|  |
"   ____| | |  | \   | |  []  |  |  |   |  |
"  |______| \__/  \__/ \______/  \__/   \__/
  

set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set mouse=a
"set relativenumber
set bg=dark
set path+=**
set wildmenu
"set ignorecase   """ / A or a is the same on search
set incsearch
set nohlsearch
set nobackup
set noswapfile
set smarttab
set shiftwidth=4
set nocompatible
set clipboard+=unnamedplus  "" copy to your system clipboard
set fillchars+=vert:\      ""vertical split line ('space' between windows)
syntax on
set shortmess=I     ""disable Vim intro message. 
set scrolloff=5     ""display several lines after EOF?
"colorscheme delek
set number
imap kj <Esc>
imap Q <q!>


call plug#begin('~/.local/share/nvim/plugged')

Plug 'http://github.com/tpope/vim-surround' " Surrounding ysw)
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/tpope/vim-commentary' " For Commenting gcc & gc
Plug 'https://github.com/vim-airline/vim-airline' " Status bar
Plug 'https://github.com/lifepillar/pgsql.vim' " PSQL Pluging needs :SQLSetType pgsql.vim
Plug 'https://github.com/ap/vim-css-color' " CSS Color Preview
Plug 'https://github.com/rafi/awesome-vim-colorschemes' " Retro Scheme
Plug 'https://github.com/neoclide/coc.nvim'  " Auto Completion
Plug 'https://github.com/ryanoasis/vim-devicons' " Developer Icons
Plug 'https://github.com/tc50cal/vim-terminal' " Vim Terminal
Plug 'https://github.com/preservim/tagbar' " Tagbar for code navigation
Plug 'https://github.com/terryma/vim-multiple-cursors' " CTRL + N for multiple cursors

set encoding=UTF-8


"Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }

call plug#end()


nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-l> :call CocActionAsync('jumpDefinition')<CR>

nmap <C-s> :TagbarToggle<CR>


" thems ---------------------
"colorscheme afterglow 
"colorscheme jellybeans
"colorscheme 256_noir
colorscheme abstract
-----------------------------
