<script lang="ts">
  import { Layout, Sidebar, UserProfile } from '@fp/layout';
  import { GitRouting } from '@fp/git/ui';
  import { DropdownMenuTrigger, DropdownMenu, DropdownMenuContent, DropdownMenuItem } from '@fp/infra/components';
  import { fpFetch } from '@fp/infra/ui/data';

  async function handleLogout() {
    await fpFetch(`/api/git/logout`, { method: 'POST' });
    window.location.reload();
  }
</script>

<Layout>
  <GitRouting/>
  {#snippet sidebar()}
    <Sidebar>
      {#snippet footer()}
        <DropdownMenu>
          <DropdownMenuTrigger>
            {#snippet child({props})}
              <button {...props}>
                <UserProfile />
              </button>
            {/snippet}
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuItem onSelect={handleLogout}>Logout</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      {/snippet}
    </Sidebar>
  {/snippet}
</Layout>
