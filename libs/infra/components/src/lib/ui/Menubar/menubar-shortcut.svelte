<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import type { WithElementRef } from "@fp/infra-components/lib/utils.js";

	let {
		ref = $bindable(null),
		children,
		...restProps
	}: WithElementRef<HTMLAttributes<HTMLSpanElement>> = $props();
</script>

<span
	bind:this={ref}
	data-slot="menubar-shortcut"
	{...restProps}
>
	{@render children?.()}
</span>
<style lang="scss">
    [data-slot="menubar-shortcut"] {
        color: var(--muted-foreground);
        margin-left: auto;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
    }
</style>