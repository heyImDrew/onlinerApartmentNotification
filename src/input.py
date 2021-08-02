from src.printstyle import PrintStyle


def get_user_input():

    # Input 'Enter start price value:'
    price_from = input(
        f"{PrintStyle.WARNING}Enter "
        f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}start price{PrintStyle.ENDC}"
        f"{PrintStyle.WARNING} value (usd): {PrintStyle.ENDC}"
    )

    # Input 'Enter end price value:'
    price_to = input(
        f"{PrintStyle.WARNING}Enter "
        f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}end price{PrintStyle.ENDC}"
        f"{PrintStyle.WARNING} value (usd): {PrintStyle.ENDC}"
    )

    # Input 'Enter only owner value:'
    only_owner_input = input(
        f"{PrintStyle.WARNING}Enter "
        f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}only owner{PrintStyle.ENDC}"
        f"{PrintStyle.WARNING} value (y/n): {PrintStyle.ENDC}"
    )

    # Input 'Enter delay value (sec):'
    delay = input(
        f"{PrintStyle.WARNING}Enter "
        f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}delay{PrintStyle.ENDC}"
        f"{PrintStyle.WARNING} value (sec): {PrintStyle.ENDC}"
    )

    return {
        'price_from': str(price_from),
        'price_to': str(price_to),
        'only_owner': 'true' if only_owner_input in ('y', 'Y', 'yes', 'YES') else None,
        'delay': int(delay)
    }
