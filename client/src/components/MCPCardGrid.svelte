<script lang="ts">
    import MCPCard from './MCPCard.svelte';

    interface MCPEntry {
        id: number;
        title: string;
        description: string;
        type: string;
        vendor: string;
        vendorLogo?: string;
    }

    export let entries: MCPEntry[] = [];
    export let viewMode: 'grid' | 'list' = 'grid';
    export let sortBy: string = 'name';

    let displayEntries = entries;

    $: {
        displayEntries = [...entries];
        
        // Sort entries
        if (sortBy === 'name') {
            displayEntries.sort((a, b) => a.title.localeCompare(b.title));
        } else if (sortBy === 'vendor') {
            displayEntries.sort((a, b) => a.vendor.localeCompare(b.vendor));
        }
    }
</script>

<div class="space-y-6">
    {#if displayEntries.length === 0}
        <div class="text-center py-12">
            <p class="text-slate-400 text-lg">No MCP servers found matching your criteria.</p>
        </div>
    {:else}
        <div class={viewMode === 'grid' ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6' : 'space-y-4'}>
            {#each displayEntries as entry (entry.id)}
                <MCPCard
                    title={entry.title}
                    description={entry.description}
                    type={entry.type}
                    vendor={entry.vendor}
                    vendorLogo={entry.vendorLogo || ""}
                />
            {/each}
        </div>
    {/if}
</div>
