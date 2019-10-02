import os
import subprocess


class Shell:

    @staticmethod
    def execute_shell_command(cmd, work_dir='.'):
        """Executes a shell command in a subprocess, waiting until it has completed.

        :param cmd: Command to execute.
        :param work_dir: Working directory path.
        """
        if isinstance(cmd, str):
            cmd = cmd.split()

        work_dir = os.path.expanduser(work_dir)

        subprocess.run(cmd, cwd=work_dir)

    @staticmethod
    def git_add(file_path, repo_dir='.'):
        """Adds the file at supplied path to the Git index.
        File will not be copied to the repository directory.
        No control is performed to ensure that the file is located in the repository directory.

        :param file_path: Path to file to add to Git index.
        :param repo_dir: Repository directory.
        """
        cmd = f'git add {file_path}'
        Shell.execute_shell_command(cmd, repo_dir)

    @staticmethod
    def git_commit(commit_message, repo_dir='.'):
        """Commits the Git repository located in supplied repository directory with the supplied commit message.

        :param commit_message: Commit message.
        :param repo_dir: Directory containing Git repository to commit.
        """
        cmd = f'git commit -am {commit_message}'
        Shell.execute_shell_command(cmd, repo_dir)

    @staticmethod
    def git_push(repo_dir):
        """Pushes any changes in the Git repository located in supplied repository directory to remote git repository.

        :param repo_dir: Directory containing git repository to push.
        """
        cmd = 'git push'
        Shell.execute_shell_command(cmd, repo_dir)

    @staticmethod
    def git_clone(repo_url, repo_dir='.'):
        """Clones the remote Git repository at supplied URL into the local directory at supplied path.
        The local directory to which the repository is to be clone is assumed to be empty.

        :param repo_url: URL of remote git repository.
        :param repo_dir: Directory which to clone the remote repository into.
        """
        cmd = f'git clone {repo_url}'
        Shell.execute_shell_command(cmd, repo_dir)
