import {
    ActionIcon,
    createStyles,
    Grid,
    Progress,
    Text,
    Title,
} from '@mantine/core';
import type { NextPage } from 'next';
import { useState } from 'react';
import type { Swiper as SwiperType } from 'swiper';
import {
    Autoplay,
    EffectFade,
    Mousewheel,
    Navigation,
    Pagination as SwiperPagination,
} from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';

import { MainHero } from '@/components/swiper/MainHero';

const useStyles = createStyles((theme) => ({
    swiper__mainhero__pagination: {
        display: 'flex',
        justifyContent: 'center',

        [theme.fn.smallerThan('md')]: {
            width: 150,
        },
        [theme.fn.largerThan('md')]: {
            width: 270,
        },
    },
}));

const Home: NextPage = () => {
    const [swiper, setSwiper] = useState<SwiperType | null>(null);
    const [mainHeroSwiper, setMainHeroSwiper] = useState<SwiperType | null>(
        null
    );
    const [mainHeroSwiperActiveIndex, setMainHeroSwiperActiveIndex] =
        useState<number>(0);

    const { classes } = useStyles();

    return (
        <>
            <Swiper
                speed={600}
                spaceBetween={0}
                direction="vertical"
                slidesPerView="auto"
                modules={[Mousewheel]}
                mousewheel={{ sensitivity: 0.001 }}
                simulateTouch={false}
                onSwiper={setSwiper}
            >
                <SwiperSlide>
                    <Swiper
                        modules={[
                            EffectFade,
                            Autoplay,
                            Navigation,
                            SwiperPagination,
                        ]}
                        effect="fade"
                        direction="horizontal"
                        autoplay={{
                            delay: 10 * 1000, // 10 secs
                        }}
                        navigation={{
                            nextEl: '.mainhero__next__el',
                            prevEl: '.mainhero__previous__el',
                        }}
                        pagination={{
                            enabled: true,
                            el: '.swiper__mainhero__pagination',
                        }}
                        onSwiper={setMainHeroSwiper}
                        onSlideChange={(swiper) => {
                            setMainHeroSwiperActiveIndex(swiper.realIndex);
                        }}
                    >
                        <SwiperSlide>
                            <MainHero
                                swiper={swiper}
                                animeTitle="Hyouka"
                                animeSummary={`High school freshman Houtarou Oreki has but one goal:High school freshman Houtarou Oreki has but one goal: to lead a gray life while conserving as much energy as he can. Unfortunately, his peaceful days come to an end when his older sister, Tomoe, forces him to save the memberless Classics Club from disbandment.\n\nLuckily, Oreki's predicament seems to be over when he heads to the clubroom and discovers that his fellow first-year, Eru Chitanda, has already become a member. However, despite his obligation being fulfilled, Oreki finds himself entangled by Chitanda's curious and bubbly personality, soon joining the club of his own volition.\n\nHyouka follows the four members of the Classics Club—including Oreki's friends Satoshi Fukube and Mayaka Ibara—as they, driven by Chitanda's insatiable curiosity, solve the trivial yet intriguing mysteries that permeate their daily lives.`}
                                backgroundImage="/images/Hyouka-poster.png"
                                backgroundBanner="https://media.kitsu.io/anime/poster_images/6686/large.jpg"
                            />
                        </SwiperSlide>
                        <SwiperSlide>
                            <MainHero
                                swiper={swiper}
                                animeTitle="KonoSuba"
                                animeSummary={`After dying a laughable and pathetic death on his way back from buying a game, high school student and recluse Kazuma Satou finds himself sitting before a beautiful but obnoxious goddess named Aqua. She provides the NEET with two options: continue on to heaven or reincarnate in every gamer's dream—a real fantasy world! Choosing to start a new life, Kazuma is quickly tasked with defeating a Demon King who is terrorizing villages. But before he goes, he can choose one item of any kind to aid him in his quest, and the future hero selects Aqua. But Kazuma has made a grave mistake—Aqua is completely useless!\n\nUnfortunately, their troubles don't end here; it turns out that living in such a world is far different from how it plays out in a game. Instead of going on a thrilling adventure, the duo must first work to pay for their living expenses. Indeed, their misfortunes have only just begun!`}
                                backgroundImage="/images/Konosuba-poster.jpg"
                                backgroundBanner="https://media.kitsu.io/anime/poster_images/10941/large.jpg"
                            />
                        </SwiperSlide>
                    </Swiper>
                </SwiperSlide>
            </Swiper>
            <Title
                sx={() => ({
                    minHeight: '10vh',
                    backgroundColor: 'rgb(7, 5, 25)',
                    display: 'flex',
                })}
            >
                <Grid
                    grow
                    justify="space-between"
                    align="center"
                    sx={() => ({
                        height: '100%',
                        width: '100%',
                    })}
                >
                    <Grid.Col
                        span={3}
                        sx={(theme) => ({
                            [theme.fn.smallerThan('md')]: {
                                display: 'none',
                            },
                        })}
                    />
                    <Grid.Col
                        span={3}
                        sx={() => ({
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            height: '10vh',
                            maxWidth: '100vw',
                            flexDirection: 'row',
                        })}
                    >
                        <Progress
                            sx={() => ({ width: 100 })}
                            mr="xl"
                            color="yellow"
                            value={
                                (100 / (mainHeroSwiper?.slides?.length ?? 0) +
                                    1) *
                                mainHeroSwiperActiveIndex
                            }
                        />
                        <div className={classes.swiper__mainhero__pagination}>
                            <div
                                style={{
                                    display: 'flex',
                                    justifyContent: 'center',
                                }}
                                className="swiper__mainhero__pagination"
                            ></div>
                        </div>
                        <ActionIcon
                            color="yellow"
                            size="lg"
                            radius="md"
                            variant="filled"
                            onClick={() => {
                                mainHeroSwiper?.slidePrev();
                            }}
                            sx={(theme) => ({
                                [theme.fn.smallerThan('md')]: {
                                    display: 'none',
                                },
                            })}
                        >
                            <img src="icons/chevron-left-black.svg" alt="" />
                        </ActionIcon>
                        <ActionIcon
                            color="yellow"
                            size="lg"
                            radius="md"
                            variant="filled"
                            ml="xl"
                            onClick={() => {
                                mainHeroSwiper?.slideNext();
                            }}
                            sx={(theme) => ({
                                [theme.fn.smallerThan('md')]: {
                                    display: 'none',
                                },
                            })}
                        >
                            <img src="icons/chevron-right-black.svg" alt="" />
                        </ActionIcon>
                    </Grid.Col>
                    <Grid.Col
                        span={3}
                        sx={(theme) => ({
                            display: 'flex',
                            justifyContent: 'flex-end',

                            [theme.fn.smallerThan('md')]: {
                                display: 'none',
                            },
                        })}
                    >
                        <img
                            width={24}
                            height={24}
                            src="/icons/mouse.svg"
                            alt=""
                        />
                        <Text px="xl" color="gray">
                            scroll below
                        </Text>
                    </Grid.Col>
                </Grid>
            </Title>
        </>
    );
};

export default Home;
