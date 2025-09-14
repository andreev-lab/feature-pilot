<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import type { WithElementRef } from "@fp/infra-components/lib/utils.js";

	let {
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	}: WithElementRef<HTMLAttributes<HTMLSpanElement>> = $props();
</script>

<style lang="scss">
    [data-slot="dropdown-menu-shortcut"] {
        color: var(--muted-foreground);
        margin-left: auto;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
    }
</style>

<span
	bind:this={ref}
	data-slot="dropdown-menu-shortcut"
	class={className}
	{...restProps}
>
	{@render children?.()}
</span>