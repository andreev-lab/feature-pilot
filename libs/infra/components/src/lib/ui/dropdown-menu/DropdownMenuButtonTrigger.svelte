<script lang="ts">
  import { Button } from '../button';
  import type {ButtonProps} from '../button'
  import DropdownMenuTrigger from './DropdownMenuTrigger.svelte';
  import type { Snippet } from 'svelte';
  import type { DropdownMenuTriggerProps } from 'bits-ui';

  type Props = {
    children: Snippet;
    trigger: DropdownMenuTriggerProps,
    button: ButtonProps
  };

  const { children, trigger, button } = $props<Props>();
</script>

<DropdownMenuTrigger {...trigger}>
  {#snippet child({ props })}
    <Button {...props} {...button}>
      {@render children()}
    </Button>
  {/snippet}
</DropdownMenuTrigger>
