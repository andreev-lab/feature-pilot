<script lang="ts">
  import type { Snippet } from 'svelte';

  let { children }: { children: Snippet } = $props();
</script>

<div class="layout">
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
    <div class="user-profile">
      <img src="https://i.pravatar.cc/40" alt="User Avatar" class="avatar" />
      <div class="user-info">
        <span class="user-name">John Doe</span>
        <span class="user-role">Administrator</span>
      </div>
    </div>
  </aside>
  <main class="main-content">
    {@render children?.()}
  </main>
</div>

<style lang="scss">
  .layout {
    display: flex;
    height: 100vh;
    background-color: #f4f7fa;
  }

  .sidebar {
    width: 250px;
    background-color: #1a202c;
    color: #e2e8f0;
    display: flex;
    flex-direction: column;
    padding: 1.5rem;
  }

  .sidebar-header {
    margin-bottom: 2rem;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 1.25rem;
    font-weight: 600;
    color: #e2e8f0;
    text-decoration: none;

    &:hover {
      color: #ffffff;
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
      padding: 0.75rem 1rem;
      border-radius: 0.375rem;
      color: #a0aec0;
      text-decoration: none;
      transition: background-color 0.2s, color 0.2s;

      &:hover {
        background-color: #2d3748;
        color: #ffffff;
      }
    }
  }

  .user-profile {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding-top: 1.5rem;
    border-top: 1px solid #2d3748;
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
    color: #ffffff;
  }

  .user-role {
    font-size: 0.875rem;
    color: #a0aec0;
  }

  .main-content {
    flex-grow: 1;
    padding: 2rem;
    overflow-y: auto;
  }
</style>
