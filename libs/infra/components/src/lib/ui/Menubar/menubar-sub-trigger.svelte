<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";
	import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
	import type { WithoutChild } from "@fp/infra-components/lib/utils.js";

	let {
		ref = $bindable(null),
		inset = undefined,
		children,
		...restProps
	}: WithoutChild<MenubarPrimitive.SubTriggerProps> & {
		inset?: boolean;
	} = $props();
</script>

<MenubarPrimitive.SubTrigger
	bind:ref
	data-slot="menubar-sub-trigger"
	data-inset={inset}
	{...restProps}
>
	{@render children?.()}
	<ChevronRightIcon />
</MenubarPrimitive.SubTrigger>
<style lang="scss">
    [data-slot="menubar-sub-trigger"] {
        display: flex;
        cursor: default;
        user-select: none;
        align-items: center;
        border-radius: var(--radius-sm);
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        outline: none;

        &:focus,
        &[data-state="open"] {
            background-color: var(--accent);
            color: var(--accent-foreground);
        }

        &[data-inset] {
            padding-left: 2rem;
        }

        :global(svg) {
            margin-left: auto;
            width: 1rem;
            height: 1rem;
        }
    }
</style>