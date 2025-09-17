<script lang="ts">
	import type { WithElementRef } from "@fp/infra-components/lib/utils.js";
	import type { HTMLAttributes } from "svelte/elements";
  import { clsx } from '@fp/infra/ui/data';

	let {
		ref = $bindable(null),
		class: className,
		inset,
		children,
		...restProps
	}: WithElementRef<HTMLAttributes<HTMLDivElement>> & {
		inset?: boolean;
	} = $props();
</script>

<style lang="scss">
    .dropdown-menu-label {
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        font-weight: 600;

        &.inset {
            padding-left: 2rem;
        }
    }
</style>

<div
	bind:this={ref}
	class={clsx("dropdown-menu-label", inset && "inset", className)}
	{...restProps}
>
	{@render children?.()}
</div>