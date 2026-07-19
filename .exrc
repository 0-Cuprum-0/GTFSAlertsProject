let s:cpo_save=&cpo
set cpo&vim
inoremap <C-W> u
inoremap <C-U> u
nnoremap 	 :bnext
nnoremap  <Cmd>nohlsearch|diffupdate|normal! 
nmap  d
nnoremap  vh <Cmd>FzfLua helptags
nnoremap  fO <Cmd>FzfLua nvim_options
nnoremap  gbr <Cmd>FzfLua git_branches
nnoremap  gbl <Cmd>FzfLua git_blame
nnoremap  gC <Cmd>FzfLua git_bcommits
nnoremap  gc <Cmd>FzfLua git_commits
nnoremap  gd <Cmd>FzfLua git_diff
nnoremap  gsa <Cmd>FzfLua git_status
nnoremap  fa <Cmd>FzfLua autocmds
nnoremap  fo <Cmd>FzfLua oldfiles
nnoremap    <Cmd>FzfLua files
nnoremap  fb <Cmd>FzfLua buffers
nnoremap  fr <Cmd>FzfLua resume
nnoremap  fW <Cmd>FzfLua grep_cWORD
nnoremap  fw <Cmd>FzfLua grep_cword
xnoremap  fv <Cmd>FzfLua grep_visual
nnoremap  fd <Cmd>FzfLua diagnostics_document
nnoremap  fc <Cmd>FzfLua lgrep_curbuf
nnoremap  fg <Cmd>FzfLua grep
nnoremap  / <Cmd>FzfLua live_grep
nnoremap  pr :Project recents
nnoremap  c :bp | bd #
nnoremap  lg :FzfLua live_grep
nnoremap  3 :tabn 3
nnoremap  2 :tabn 2
nnoremap  1 :tabn 1
nnoremap  y :Yazi
nnoremap  e <Cmd>NvimTreeToggle
omap <silent> % <Plug>(MatchitOperationForward)
xmap <silent> % <Plug>(MatchitVisualForward)
nmap <silent> % <Plug>(MatchitNormalForward)
nnoremap & :&&
xnoremap <silent> <expr> @ mode() ==# 'V' ? ':normal! @'.getcharstr().'' : '@'
xnoremap <silent> <expr> Q mode() ==# 'V' ? ':normal! @=reg_recorded()' : 'Q'
nnoremap Y y$
omap <silent> [% <Plug>(MatchitOperationMultiBackward)
xmap <silent> [% <Plug>(MatchitVisualMultiBackward)
nmap <silent> [% <Plug>(MatchitNormalMultiBackward)
omap <silent> ]% <Plug>(MatchitOperationMultiForward)
xmap <silent> ]% <Plug>(MatchitVisualMultiForward)
nmap <silent> ]% <Plug>(MatchitNormalMultiForward)
xmap a% <Plug>(MatchitVisualTextObject)
omap <silent> g% <Plug>(MatchitOperationBackward)
xmap <silent> g% <Plug>(MatchitVisualBackward)
nmap <silent> g% <Plug>(MatchitNormalBackward)
xmap <silent> <Plug>(MatchitVisualTextObject) <Plug>(MatchitVisualMultiBackward)o<Plug>(MatchitVisualMultiForward)
onoremap <silent> <Plug>(MatchitOperationMultiForward) :call matchit#MultiMatch("W",  "o")
onoremap <silent> <Plug>(MatchitOperationMultiBackward) :call matchit#MultiMatch("bW", "o")
xnoremap <silent> <Plug>(MatchitVisualMultiForward) :call matchit#MultiMatch("W",  "n")m'gv``
xnoremap <silent> <Plug>(MatchitVisualMultiBackward) :call matchit#MultiMatch("bW", "n")m'gv``
nnoremap <silent> <Plug>(MatchitNormalMultiForward) :call matchit#MultiMatch("W",  "n")
nnoremap <silent> <Plug>(MatchitNormalMultiBackward) :call matchit#MultiMatch("bW", "n")
onoremap <silent> <Plug>(MatchitOperationBackward) :call matchit#Match_wrapper('',0,'o')
onoremap <silent> <Plug>(MatchitOperationForward) :call matchit#Match_wrapper('',1,'o')
xnoremap <silent> <Plug>(MatchitVisualBackward) :call matchit#Match_wrapper('',0,'v')m'gv``
xnoremap <silent> <Plug>(MatchitVisualForward) :call matchit#Match_wrapper('',1,'v'):if col("''") != col("$") | exe ":normal! m'" | endifgv``
nnoremap <silent> <Plug>(MatchitNormalBackward) :call matchit#Match_wrapper('',0,'n')
nnoremap <silent> <Plug>(MatchitNormalForward) :call matchit#Match_wrapper('',1,'n')
nnoremap <S-Tab> :bp
nmap <C-W><C-D> d
nnoremap <C-L> <Cmd>nohlsearch|diffupdate|normal! 
inoremap <expr>  v:lua.require'nvim-autopairs'.completion_confirm()
inoremap  u
inoremap  u
let &cpo=s:cpo_save
unlet s:cpo_save
set clipboard=unnamedplus
set completeopt=menuone,noinsert,noselect
set grepformat=%f:%l:%c:%m
set grepprg=rg\ --vimgrep\ -uu\ 
set helplang=en
set laststatus=3
set noloadplugins
set packpath=/nix/store/fvrp5xsx4870n75nj8scdhnkqxvn9xj9-neovim-unwrapped-0.11.7/share/nvim/runtime
set runtimepath=~/.config/nvim,~/.local/share/nvim/site,~/.local/share/nvim/lazy/lazy.nvim,~/.local/share/nvim/lazy/nvim-autopairs,~/.local/share/nvim/lazy/snacks.nvim,~/.local/share/nvim/lazy/vimtex,~/.local/share/nvim/lazy/nvim-lspconfig,~/.local/share/nvim/lazy/nvim-tree.lua,~/.local/share/nvim/lazy/nvim-treesitter,~/.local/share/nvim/lazy/render-markdown.nvim,~/.local/share/nvim/lazy/lualine.nvim,~/.local/share/nvim/lazy/mini.nvim,~/.local/share/nvim/lazy/alpha-nvim,~/.local/share/nvim/lazy/luatab.nvim,~/.local/share/nvim/lazy/mason.nvim,~/.local/share/nvim/lazy/mason-lspconfig.nvim,~/.local/share/nvim/lazy/nvim-web-devicons,~/.local/share/nvim/lazy/fzf-lua,~/.local/share/nvim/lazy/project.nvim,~/.local/share/nvim/lazy/scope.nvim,~/.local/share/nvim/lazy/friendly-snippets,~/.local/share/nvim/lazy/blink.cmp,/nix/store/fvrp5xsx4870n75nj8scdhnkqxvn9xj9-neovim-unwrapped-0.11.7/share/nvim/runtime,/nix/store/fvrp5xsx4870n75nj8scdhnkqxvn9xj9-neovim-unwrapped-0.11.7/share/nvim/runtime/pack/dist/opt/matchit,/nix/store/fvrp5xsx4870n75nj8scdhnkqxvn9xj9-neovim-unwrapped-0.11.7/lib/nvim,~/.local/state/nvim/lazy/readme,~/.local/share/nvim/lazy/vimtex/after,~/.local/share/nvim/lazy/mason-lspconfig.nvim/after
set scrolloff=10
set shell=bash
set showtabline=2
set statusline=%#lualine_transparent#
set tabline=%!v:lua.require'luatab'.helpers.tabline()
set termguicolors
set undofile
set wildignore=*.pyc
set window=56
" vim: set ft=vim :
