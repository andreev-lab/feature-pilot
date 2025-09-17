## Usage example

```sveltehtml
<script lang="ts">
  import { Button } from '@fp/infra-components/lib/ui/button';
  import {
    DropdownMenu,
    DropdownMenuSub,
    DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem,
    DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuShortcut, DropdownMenuSubContent, DropdownMenuSubTrigger,
    DropdownMenuButtonTrigger
  } from '@fp/infra-components/lib/ui/dropdown-menu';
</script>

<DropdownMenu>
  <DropdownMenuButtonTrigger>
    Open
  </DropdownMenuButtonTrigger>
  <DropdownMenuContent class="w-56" align="start">
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuGroup>
      <DropdownMenuItem onSelect={() => console.log('Profile clicked')}>
        Profile
        <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
      </DropdownMenuItem>
      <DropdownMenuItem onSelect={() => console.log('Billing clicked')}>
        Billing
        <DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
      </DropdownMenuItem>
      <DropdownMenuItem onSelect={() => console.log('Settings clicked')}>
        Settings
        <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
      </DropdownMenuItem>
      <DropdownMenuItem onSelect={() => console.log('Keyboard shortcuts clicked')}>
        Keyboard shortcuts
        <DropdownMenuShortcut>⌘K</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem onSelect={() => console.log('Team clicked')}>Team</DropdownMenuItem>
      <DropdownMenuSub>
        <DropdownMenuSubTrigger>Invite users</DropdownMenuSubTrigger>
        <DropdownMenuSubContent>
          <DropdownMenuItem onSelect={() => console.log('Email clicked')}>Email</DropdownMenuItem>
          <DropdownMenuItem onSelect={() => console.log('Message clicked')}>Message</DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem onSelect={() => console.log('More... clicked')}>More...</DropdownMenuItem>
        </DropdownMenuSubContent>
      </DropdownMenuSub>
      <DropdownMenuItem onSelect={() => console.log('New Team clicked')}>
        New Team
        <DropdownMenuShortcut>⌘+T</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuItem onSelect={() => console.log('GitHub clicked')}>GitHub</DropdownMenuItem>
    <DropdownMenuItem onSelect={() => console.log('Support clicked')}>Support</DropdownMenuItem>
    <DropdownMenuItem disabled>API</DropdownMenuItem>
    <DropdownMenuSeparator />
    <DropdownMenuItem onSelect={() => console.log('Log out clicked')}>
      Log out
      <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
    </DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

## Advanced Usage

### Custom Trigger

For more advanced use cases, you can use the `DropdownMenuTrigger` component and provide your own button or other trigger element.

```sveltehtml
<script lang="ts">
  import { Button } from '@fp/infra-components/lib/ui/button';
  import {
    DropdownMenu,
    DropdownMenuSub,
    DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem,
    DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuShortcut, DropdownMenuSubContent, DropdownMenuSubTrigger,
    DropdownMenuTrigger
  } from '@fp/infra-components/lib/ui/dropdown-menu';
</script>

<DropdownMenu>
  <DropdownMenuTrigger>
    {#snippet child({props})}
      <Button {...props} variant="outline">Custom Trigger</Button>
    {/snippet}
  </DropdownMenuTrigger>
  <DropdownMenuContent class="w-56" align="start">
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuGroup>
      <DropdownMenuItem>
        Profile
        <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenuContent>
</DropdownMenu>
```