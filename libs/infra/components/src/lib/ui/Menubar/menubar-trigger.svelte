<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		...restProps
	}: MenubarPrimitive.TriggerProps = $props();
</script>

<MenubarPrimitive.Trigger
	bind:ref
	data-slot="menubar-trigger"
	{...restProps}
/>
<style lang="scss">
    [data-slot="menubar-trigger"] {
        display: flex;
        user-select: none;
        align-items: center;
        border-radius: var(--radius-sm);
        padding: 0.25rem 0.5rem;
        font-size: 0.875rem;
        font-weight: 500;
        outline: none;

        &:focus,
        &[data-state="open"] {
            background-color: var(--accent);
            color: var(--accent-foreground);
        }
    }
</style>