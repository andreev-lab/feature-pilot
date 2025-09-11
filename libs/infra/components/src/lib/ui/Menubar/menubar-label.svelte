<script lang="ts">
	import { type WithElementRef } from "bits-ui";
	import type { HTMLAttributes } from "svelte/elements";

	let {
		ref = $bindable(null),
		inset,
		children,
		...restProps
	}: WithElementRef<HTMLAttributes<HTMLElement>> & {
		inset?: boolean;
	} = $props();
</script>

<div
	bind:this={ref}
	data-slot="menubar-label"
	data-inset={inset}
	{...restProps}
>
	{@render children?.()}
</div>
<style lang="scss">
    [data-slot="menubar-label"] {
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;

        &[data-inset] {
            padding-left: 2rem;
        }
    }
</style>