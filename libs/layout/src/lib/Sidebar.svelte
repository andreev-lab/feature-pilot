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
    background-color: var(--color-primary);
    color: var(--color-primary-foreground);
    display: flex;
    flex-direction: column;
    padding: var(--fp-distance-6);
    border-right: 1px solid oklch(from var(--color-primary-foreground) l c h / 0.1);
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
    color: var(--color-primary-foreground);
    text-decoration: none;

    &:hover {
      color: var(--color-primary-foreground);
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
      color: oklch(from var(--color-primary-foreground) l c h / 0.75);
      text-decoration: none;
      transition: background-color 0.2s, color 0.2s;

      &:hover {
        background-color: oklch(from var(--color-primary) calc(l + 0.07) c h);
        color: var(--color-primary-foreground);
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
    color: var(--color-primary-foreground);
    padding: var(--fp-distance-2);
    border-radius: var(--radius-md);


    &:hover {
      background-color: oklch(from var(--color-primary) calc(l + 0.07) c h);
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
    color: var(--color-primary-foreground);
  }

  .user-role {
    font-size: 0.875rem;
    color: oklch(from var(--color-primary-foreground) l c h / 0.6);
  }
</style>
