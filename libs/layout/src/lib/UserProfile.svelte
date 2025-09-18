<script>
</script>

<style lang="sass">
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

<div class="user-profile">
  <img src="https://i.pravatar.cc/40" alt="User Avatar" class="avatar" />
  <div class="user-info">
    <span class="user-name">John Doe</span>
    <span class="user-role">Administrator</span>
  </div>
</div>
