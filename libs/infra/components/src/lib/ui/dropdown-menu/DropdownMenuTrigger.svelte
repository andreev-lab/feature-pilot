<script lang="ts">
	import { DropdownMenu as DropdownMenuPrimitive } from "bits-ui";
  import { clsx } from '@fp/infra/ui/data';

	let {
    ref = $bindable(null),
    class: className,
    ...restProps
  }: DropdownMenuPrimitive.TriggerProps & { class?: string; } = $props();
</script>

<DropdownMenuPrimitive.Trigger bind:ref class={clsx("dropdown-menu-trigger", className)} {...restProps} />
