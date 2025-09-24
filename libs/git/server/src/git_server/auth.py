from fastapi import Depends, HTTPException
import reactivex.operators as ops

from git_server.sdk.data import FpAuthRes
from git_server.sdk.github_sdk import GithubSdk, inject_github_sdk


class AuthChecker:
  async def __call__(self, github_sdk: GithubSdk = Depends(inject_github_sdk)):
    try:
      is_auth: FpAuthRes = await github_sdk.auth_state().pipe(ops.to_future())
      print(f"auth: {is_auth.is_authenticated}")
      if not is_auth.is_authenticated:
        raise HTTPException(status_code=401, detail="Not authenticated")
    except Exception as e:
      print("user is not authenticated")
      raise HTTPException(status_code=401, detail="Not authenticated") from e

require_auth = AuthChecker()
