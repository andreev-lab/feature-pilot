<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";

	let {
		ref = $bindable(null),
		inset = undefined,
		variant = "default",
		...restProps
	}: MenubarPrimitive.ItemProps & {
		inset?: boolean;
		variant?: "default" | "destructive";
	} = $props();
</script>

<MenubarPrimitive.Item
	bind:ref
	data-slot="menubar-item"
	data-inset={inset}
	data-variant={variant}
	{...restProps}
/>
<style lang="scss">
    [data-slot="menubar-item"] {
        position: relative;
        display: flex;
        cursor: default;
        user-select: none;
        align-items: center;
        border-radius: var(--radius-sm);
        padding: 0.375rem 0.5rem;
        font-size: 0.875rem;
        outline: none;
        gap: 0.5rem;

        &:focus {
            background-color: var(--accent);
            color: var(--accent-foreground);
        }

        &[data-inset] {
            padding-left: 2rem;
        }

        &[data-disabled] {
            pointer-events: none;
            opacity: 0.5;
        }

        &[data-variant="destructive"] {
            color: var(--destructive);
            &:focus {
                background-color: rgba(var(--destructive-rgb), 0.1);
                color: var(--destructive);
            }
            :global(svg) {
                color: var(--destructive) !important;
            }
        }

        :global(svg:not([class*="text-"])) {
            color: var(--muted-foreground);
        }

        :global(svg:not([class*="size-"])) {
            width: 1rem;
            height: 1rem;
        }
        :global(svg) {
            pointer-events: none;
            flex-shrink: 0;
        }
    }
    .dark [data-slot="menubar-item"][data-variant="destructive"]:focus {
        background-color: rgba(var(--destructive-rgb), 0.2);
    }
</style>