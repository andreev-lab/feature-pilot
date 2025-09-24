<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
    ref = $bindable(null),
    class: className,
    ...restProps
  }: DropdownMenuPrimitive.GroupProps & { class?: string; } = $props();
</script>

<DropdownMenuPrimitive.Group bind:ref class={clsx("dropdown-menu-group", className)} {...restProps} />
