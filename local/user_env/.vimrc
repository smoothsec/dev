"Vimrc configuration

"call pathogen#infect()

"map <F1> :NERDTreeToggle<CR>

"autocmd FileType python map <buffer> <F4> :call Flake8()<CR>

syntax enable
filetype indent on
filetype plugin on
" f2 run python interpeter 
"map <f2> :w\|!python %<cr>
" CTRL-V select block
" f2 Insert comments
map <F2> I#<Esc><Esc>
" f3 Delete comments
map <F3> x<Esc><Esc>
"set number
set tabstop=4
set shiftwidth=4
set expandtab
"set pastetoggle=<F4>
set cursorline
set showmode
