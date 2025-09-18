<script lang="ts">
  import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger
  } from '@fp/infra-components';
  import { fpFetch } from '@fp/infra/ui/data';

  async function logout() {
    await fpFetch(`/api/git/logout`, { method: 'POST' });
    window.location.reload();
  }
</script>

<aside class="sidebar">
  <div class="sidebar-header">
    <a href="/" class="logo">
      <span>Feature Pilot</span>
    </a>
  </div>
  <nav class="navigation">
    <ul>
      <li><a href="/dashboard">Dashboard</a></li>
      <li><a href="/features">Features</a></li>
      <li><a href="/settings">Settings</a></li>
      <li><a href="/help">Help</a></li>
    </ul>
  </nav>
  <DropdownMenu>
    <DropdownMenuTrigger asChild>
      {#snippet child({ props })}
        <button {...props} class="user-profile">
          <img src="https://i.pravatar.cc/40" alt="User Avatar" class="avatar" />
          <div class="user-info">
            <span class="user-name">John Doe</span>
            <span class="user-role">Administrator</span>
          </div>
        </button>
      {/snippet}
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuItem on:select={logout}>Log out</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</aside>

<style lang="scss">
  .sidebar {
    width: 250px;
    background-color: var(--color-sidebar);
    color: var(--color-sidebar-foreground);
    display: flex;
    flex-direction: column;
    padding: var(--fp-distance-6);
    border-right: 1px solid var(--color-sidebar-border);
  }

  .sidebar-header {
    margin-bottom: var(--fp-distance-8);
  }

  .logo {
    display: flex;
    align-items: center;
    gap: var(--fp-distance-3);
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-sidebar-foreground);
    text-decoration: none;

    &:hover {
      color: var(--color-sidebar-primary-foreground);
    }
  }

  .navigation {
    flex-grow: 1;

    ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    li a {
      display: block;
      padding: var(--fp-distance-3) var(--fp-distance-4);
      border-radius: var(--radius-md);
      color: var(--color-sidebar-accent-foreground);
      text-decoration: none;
      transition: background-color 0.2s, color 0.2s;

      &:hover {
        background-color: var(--color-sidebar-accent);
        color: var(--color-sidebar-foreground);
      }
    }
  }

  .user-profile {
    display: flex;
    align-items: center;
    gap: var(--fp-distance-3);
    background: none;
    border: none;
    font: inherit;
    cursor: pointer;
    outline: inherit;
    width: 100%;
    text-align: left;
    color: var(--color-sidebar-foreground);
    padding: var(--fp-distance-2);
    border-radius: var(--radius-md);


    &:hover {
      background-color: var(--color-sidebar-accent);
    }
  }

  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }

  .user-info {
    display: flex;
    flex-direction: column;
  }

  .user-name {
    font-weight: 600;
    color: var(--color-sidebar-foreground);
  }

  .user-role {
    font-size: 0.875rem;
    color: var(--color-sidebar-accent-foreground);
  }
</style>
