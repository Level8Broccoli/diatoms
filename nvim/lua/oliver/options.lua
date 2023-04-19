-- Set highlight on search
vim.o.hlsearch = false

-- Make line numbers default
vim.wo.number = true

-- Make line numbers relative
vim.wo.relativenumber = true

-- Enable mouse mode
vim.o.mouse = 'a'

-- Sync clipboard between OS and Neovim.
vim.o.clipboard = 'unnamedplus'

-- Show tabs always (2)
vim.o.showtabline = 2

-- Set indentation to 2 spaces
vim.o.tapstop = 2
vim.o.expandtab = true
vim.o.shiftwidth = 2
vim.o.shiftround = true

-- Show line under curser
vim.o.cursorline = true

-- Enable break indent
vim.o.breakindent = true

-- Minimal number of screen lines above and below cursor
vim.o.scrolloff = 10

-- Save undo history
vim.o.undofile = true

-- Case insensitive searching UNLESS /C or capital in search
vim.o.ignorecase = true
vim.o.smartcase = true

-- Keep signcolumn on by default
vim.wo.signcolumn = 'yes'

-- Decrease update time
vim.o.updatetime = 250
vim.o.timeout = true
vim.o.timeoutlen = 300

-- Set completeopt to have a better completion experience
vim.o.completeopt = 'menuone,noselect'

-- Enables 24-bit colors
vim.o.termguicolors = true
