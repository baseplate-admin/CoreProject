<script lang="ts">
    import badgeData from "$data/components/badge_data.json";
    import ChevronDown from "$icons/Chevron-Down.svelte";
    import ChevronUpDown from "$icons/Chevron-Up-Down.svelte";
    import { responsiveMode } from "$store/Responsive";

    import AutoComplete from "./AutoComplete.svelte";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropdownGenreElementActive = false;
</script>

<div class="hero min-h-[20vh] md:min-h-screen bg-base-100">
    <div class="hero-content text-center p-0">
        <div>
            <AutoComplete />

            {#if mobile}
                <div
                    class="dropdown mt-5 dropdown-top {dropdownGenreElementActive
                        ? 'dropdown-open'
                        : ''}"
                >
                    <div
                        tabindex="0"
                        class="m-1 btn normal-case"
                        on:click={() => {
                            dropdownGenreElementActive = !dropdownGenreElementActive;
                        }}
                    >
                        or search by genres <ChevronUpDown color="#D8D8D8" height={18} width={18} />
                    </div>
                    <ul
                        tabindex="0"
                        class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 items-center inset-x-0 mx-auto pt-6"
                    >
                        {#each badgeData as item}
                            <li>{item.name}</li>
                        {/each}
                    </ul>
                </div>
            {:else}
                <div class="divider w-80 mx-auto mt-12 mb-6 before:bg-white after:bg-white">
                    or search by genres
                </div>
                <div class="grid grid-cols-6 gap-x-10 gap-y-5 justify-items-center">
                    {#each badgeData as item}
                        <div class="btn font-bold text-black w-fit whitespace-nowrap {item.class}">
                            {item.name}
                        </div>
                    {/each}
                </div>
                <div class="mt-24 flex flex-col items-center">
                    <div class="w-[500px]">
                        <h1 class="font-bold text-3xl mb-2">Choose your preferences</h1>
                        <p>
                            Choose some options to customize your experience. You can change them
                            anytime by clicking the profile icon and going to Settings
                        </p>
                    </div>
                </div>
                <div class="flex flex-col w-full lg:flex-row justify-center mt-8">
                    <div class="flex flex-row align-center">
                        Romaji Naming <ChevronDown color="white" height={30} width={30} />
                    </div>
                    <div class="divider lg:divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        10 point scoring system <ChevronDown color="white" height={30} width={30} />
                    </div>
                    <div class="divider lg:divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        2 trackers added <ChevronDown color="white" height={30} width={30} />
                    </div>
                    <div class="divider lg:divider-horizontal before:bg-white after:bg-white" />
                    <div class="flex flex-row align-center">
                        Show 18+ content <ChevronDown color="white" height={30} width={30} />
                    </div>
                </div>
            {/if}
        </div>
    </div>
</div>
