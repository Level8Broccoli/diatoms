return {
  "kdheepak/lazygit.nvim",
  config = function()
    vim.keymap.set("n", "<leader>lg", ":LazyGit<cr>", { noremap = true, silent = true })
  end,
}
