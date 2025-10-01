<script lang="ts">
    export let selectedTypes: string[] = [];
    export let selectedVendors: string[] = [];
    export let selectedEndpoints: string[] = [];
    export let onFilterChange: () => void = () => {};

    const types = ["Local", "Remote"];
    const vendors = ["Microsoft", "Partner"];
    const endpoints = ["Public"];

    function toggleFilter(array: string[], value: string) {
        const index = array.indexOf(value);
        if (index > -1) {
            array.splice(index, 1);
        } else {
            array.push(value);
        }
        selectedTypes = selectedTypes;
        selectedVendors = selectedVendors;
        selectedEndpoints = selectedEndpoints;
        onFilterChange();
    }
</script>

<div class="bg-slate-800/60 backdrop-blur-sm rounded-xl border border-slate-700/50 p-6 sticky top-6">
    <h3 class="text-lg font-semibold text-slate-100 mb-4">Filters</h3>
    
    <!-- Types -->
    <div class="mb-6">
        <h4 class="text-sm font-medium text-slate-300 mb-3">Types</h4>
        <div class="space-y-2">
            {#each types as type}
                <label class="flex items-center cursor-pointer group">
                    <input
                        type="checkbox"
                        checked={selectedTypes.includes(type)}
                        on:change={() => toggleFilter(selectedTypes, type)}
                        class="w-4 h-4 text-blue-600 bg-slate-700 border-slate-600 rounded focus:ring-blue-500 focus:ring-2 cursor-pointer"
                    />
                    <span class="ml-2 text-sm text-slate-400 group-hover:text-slate-300 transition-colors">{type}</span>
                </label>
            {/each}
        </div>
    </div>

    <!-- Vendors -->
    <div class="mb-6">
        <h4 class="text-sm font-medium text-slate-300 mb-3">Vendors</h4>
        <div class="space-y-2">
            {#each vendors as vendor}
                <label class="flex items-center cursor-pointer group">
                    <input
                        type="checkbox"
                        checked={selectedVendors.includes(vendor)}
                        on:change={() => toggleFilter(selectedVendors, vendor)}
                        class="w-4 h-4 text-blue-600 bg-slate-700 border-slate-600 rounded focus:ring-blue-500 focus:ring-2 cursor-pointer"
                    />
                    <span class="ml-2 text-sm text-slate-400 group-hover:text-slate-300 transition-colors">{vendor}</span>
                </label>
            {/each}
        </div>
    </div>

    <!-- Endpoint -->
    <div>
        <h4 class="text-sm font-medium text-slate-300 mb-3">Endpoint</h4>
        <div class="space-y-2">
            {#each endpoints as endpoint}
                <label class="flex items-center cursor-pointer group">
                    <input
                        type="checkbox"
                        checked={selectedEndpoints.includes(endpoint)}
                        on:change={() => toggleFilter(selectedEndpoints, endpoint)}
                        class="w-4 h-4 text-blue-600 bg-slate-700 border-slate-600 rounded focus:ring-blue-500 focus:ring-2 cursor-pointer"
                    />
                    <span class="ml-2 text-sm text-slate-400 group-hover:text-slate-300 transition-colors">{endpoint}</span>
                </label>
            {/each}
        </div>
    </div>
</div>
