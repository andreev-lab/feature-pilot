import os
import shutil
import subprocess
import tempfile
import unittest

from git_server.git_sdk import GitSdk


class TestGitSdkIntegration(unittest.TestCase):

  def setUp(self):
    # Create a temporary directory for the test
    self.test_dir = tempfile.mkdtemp()
    self.remote_repo_path = os.path.join(self.test_dir, 'remote_repo.git')
    self.base_dir = os.path.join(self.test_dir, 'git_sdk_repos')

    # Create a bare git repository to act as a remote
    subprocess.run(['git', 'init', '--bare', self.remote_repo_path], check=True)

    # The GitSdk will clone from this "remote"
    self.sdk = GitSdk(repo_url=self.remote_repo_path, base_dir=self.base_dir)

    # Determine the path to the cloned repository without accessing private members
    repo_name = os.path.basename(self.remote_repo_path).replace('.git', '')
    self.cloned_repo_path = os.path.join(self.base_dir, repo_name)

    # Configure git user for commits
    subprocess.run(
      ['git', 'config', 'user.email', 'test@example.com'],
      cwd=self.cloned_repo_path, check=True
    )
    subprocess.run(
      ['git', 'config', 'user.name', 'Test User'],
      cwd=self.cloned_repo_path, check=True
    )

  def tearDown(self):
    shutil.rmtree(self.test_dir)

  def test_clone(self):
    self.assertTrue(os.path.exists(os.path.join(self.cloned_repo_path, '.git')))

  def test_get_readme_found(self):
    readme_content = "This is a test README."
    readme_path = os.path.join(self.cloned_repo_path, 'README.md')
    with open(readme_path, 'w') as f:
      f.write(readme_content)
    subprocess.run(['git', 'add', 'README.md'], cwd=self.cloned_repo_path, check=True)
    subprocess.run(
      ['git', 'commit', '-m', 'Add README'],
      cwd=self.cloned_repo_path, check=True
    )

    readme = self.sdk.get_readme()

    self.assertEqual(readme, readme_content)

  def test_get_readme_not_found(self):
    readme = self.sdk.get_readme()

    self.assertEqual(readme, 'README.md not found.')

  def test_push(self):
    test_file_path = os.path.join(self.cloned_repo_path, 'test.txt')
    with open(test_file_path, 'w') as f:
      f.write('hello')
    subprocess.run(['git', 'add', 'test.txt'], cwd=self.cloned_repo_path, check=True)
    subprocess.run(
      ['git', 'commit', '-m', 'Test commit'],
      cwd=self.cloned_repo_path, check=True
    )

    commit_hash = subprocess.check_output(
      ['git', 'rev-parse', 'HEAD'], cwd=self.cloned_repo_path
    ).strip().decode()

    branch_name = subprocess.check_output(
      ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
      cwd=self.cloned_repo_path
    ).strip().decode()
    self.sdk.push(branch=branch_name)

    remote_commit_hash = subprocess.check_output(
      ['git', 'rev-parse', f'refs/heads/{branch_name}'],
      cwd=self.remote_repo_path
    ).strip().decode()
    self.assertEqual(commit_hash, remote_commit_hash)

if __name__ == '__main__':
  unittest.main()
