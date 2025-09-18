<script lang="ts">
  import { Layout, Sidebar, UserProfile } from '@fp/layout';
  import { GitRouting } from '@fp/git/ui';
  import { DropdownMenuTrigger, DropdownMenu, DropdownMenuContent, DropdownMenuItem } from '@fp/infra/components';
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
            <DropdownMenuItem onSelect={() => console.log('log out')}>Logout</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      {/snippet}
    </Sidebar>
  {/snippet}
</Layout>
