import { GitService } from '../service/git-service';

export async function isUserAuthenticated() {
  try {
    await GitService.isUserAuthedOrThrow();
    return true;
  } catch {
    return false;
  }
}
